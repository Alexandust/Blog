from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CommentForm
from blog.models import Post


@require_POST #限制该视图函数只能通过POST请求触发
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.post.commentscount()
        comment.save()
        messages.add_message(request, messages.SUCCESS, '已评论', extra_tags='success')
        return redirect(post)
    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论失败，请修改内容后重新提交', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)


