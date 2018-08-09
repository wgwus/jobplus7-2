from flask import Blueprint, render_template, flash, redirect,current_app, url_for, request, abort
from flask_login import login_required,current_user
from jobplus.forms import ComproForm
from jobplus.models import User,Company

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

@company.route('/')
def index():
    page =request.args.get('page',default=1,type=int)
    pagination = Company.query.paginate(
            page=page,
            per_page=6,#current_app.config['INDEX_PER_PAGE'],
            error_out=False)
    return render_template('company/index.html',pagination=pagination,active='company')

@company.route('/<int:company_id>')
def detail(company_id):
    company = Company.query.get_or_404(company_id)
    user = User.query.get_or_404(company_id)
    #if not company.is_company:
    #    abort(404)
       # 上面需要 models表里面建立 Role的判断 判断后才能下一步
     #   @property
     #   def is_company(self):
     #       return self.role == self.ROLE_COMPANY
    return render_template('company/detail.html',company=company)


