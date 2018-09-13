from invoke import task


@task
def code(ctx):
    ctx.run('mkdir -p ~/code')


@task
def scm(ctx):
    ctx.run('brew install git || brew upgrade git')
    ctx.run('brew cask install sourcetree')


@task
def dotfiles(ctx):
    ctx.run('git clone git@github.com:pgpbpadilla/dotfiles.git ~/code/dotfiles.git')


@task(pre=[code, scm, dotfiles])
def all(ctx):
    pass