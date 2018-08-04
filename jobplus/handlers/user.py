from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from jobplus.forms import UserproForm

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserproForm(obj=current_user)
    if form.validate_on_submit():
        form.UserupForm(current_user)
        flash('update success', 'success')
        return redirect(url_for('front.index'))
    return render_template('useprofile.html', form=form)
