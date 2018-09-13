from invoke import task


@task
def scm(ctx):
    ctx.run('brew install git || brew upgrade git')
    ctx.run('brew cask install sourcetree')


@task
def dotfiles(ctx):
    pass

@task(pre=[scm])
def all(ctx):
    pass