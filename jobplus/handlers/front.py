from flask import Blueprint, render_template,redirect,url_for,flash,request
from jobplus.models import User,db
from jobplus.forms import LoginForm, RegisterForm
from flask_login import login_user,logout_user,login_required
front = Blueprint('front', __name__)

@front.route('/')
def index():
    
    return render_template('index.html')

@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user,form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)


@front.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录!','success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)

@front.route('/comregister', methods=['GET', 'POST'])
def Comregister():
    form = RegisterForm()
    form.username.label = u'企业名称'
    if form.validate_on_submit():
        company_user = form.create_user()
        company_user.role = User.ROLE_Company
        db.session.add(company_user)
        db.session.commit()
        flash('注册成功,清登录', 'success')
        return redirect(url_for('.login'))
    return render_template('comregister.html', form=form)





@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录','success')
    return redirect(url_for('.index'))
