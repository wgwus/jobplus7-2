from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,TextAreaField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User,Company


class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(4,12)])
    email = StringField('邮箱', validators=[Required(), Email()])   
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('确认密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
                raise ValidationError('用户名已存在')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
                raise ValidationError('邮箱已存在')
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user) 
        db.session.commit()
        return user
class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')
    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class UserproForm(FlaskForm):

    real_name = StringField('姓名')
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    work_year = StringField('工作经验')
    phone = StringField('手机号码')
    resume_url = StringField('简历')
    submit = SubmitField('提交')
    def validate_phone(self,field):
        if field.data[:2] not in ('13','15','18') and len(field.data)!=11:
           raise ValidationError('请输入正确的手机号')
    
    def UserupForm(self,user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
           user.password = self.password.data
        user.work_year = self.work_year.data
        user.phone = self.phone.data
        user.resume_url = self.resume_url.data
     
        db.session.add(user)
        db.session.commit()
class ComproForm(FlaskForm):
    name = StringField('公司名称') 
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码')
    location = StringField('公司地址',validators=[Required(),Length(0,64)])
    website = StringField('公司主页',validators=[Required(),Length(0,64)])
    logo = StringField('公司Logo',validators=[Required(),Length(0,128)])
    description = StringField('一句话描述',validators=[Length(0,100)])
    about = TextAreaField('关于公司',validators=[Length(0,1024)])
    submit = SubmitField('提交')

    def ComupForm(self,user):
       user.username = self.name.data
       user.email = self.email.data
       user.role = 20
       if self.password.data:
          user.password = self.password.data
       if user.company:
          company = user.company
       else:
          company = Company()
          company.user_id = user.id
       self.populate_obj(company)  
       db.session.add(user)
       db.session.add(company)
       db.session.commit()
