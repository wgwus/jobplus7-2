from flask import Blueprint, render_template, flash, redirect,current_app, url_for, request, abort
from flask_login import login_required,current_user
from jobplus.forms import ComproForm
from jobplus.models import User,Company,Job,Dilivery,db


job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    page =request.args.get('page',default=1,type=int)
    # 倒序
    pagination = Job.query.order_by(Job.created_at.desc()).paginate(
            page=page,
            per_page=9,#current_app.config['INDEX_PER_PAGE'],
            error_out=False)
    return render_template('job/index.html',pagination=pagination,active=job)
@job.route('/<int:job_id>')
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html',job=job)

@job.route('/<int:job_id>/apply')
@login_required
def apply(job_id):
    job = Job.query.get_or_404(job_id)
    #models 添加函数
    if job.current_user_is_applied:
        flash('已经投递','warning')
    else:
        d = Dilivery(job_id=job.id,user_id=current_user.id)
        db.session.add(d)
        db.session.commit()
        flash('已经投递','successd')
    return redirect(url_for('job.detail',job_id=job.id))

