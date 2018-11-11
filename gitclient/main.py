from git import Repo


if __name__ == '__main__':
    repo=Repo('')

    # 新建版本库对象
    repo = Repo(r'E:\Notes')

    # 进行文件修改操作

    # 获取版本库暂存区
    index = repo.index
    # 添加修改文件
    index.add(['new.txt'])
    # 提交修改到本地仓库
    index.commit('this is a test')

    # 获取远程仓库
    remote = repo.remote()
    # 推送本地修改到远程仓库
    remote.push()