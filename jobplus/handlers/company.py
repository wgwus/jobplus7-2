from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from jobplus.forms import ComproForm

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('error', 'warning')
        return redirect(url_for('front.index'))
    form = ComproForm(obj=current_user.company)
    form.name.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.ComupForm(current_user)
        flash('success', 'success')
        return redirect(url_for('front.index'))
    return render_template('comprofile.html', form=form)
