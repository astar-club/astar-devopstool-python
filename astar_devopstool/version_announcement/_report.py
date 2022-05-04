#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: report .py
# @time: 2020/12/4 14:45
# @Software: PyCharm


from astartool.project import auto_title
from astartool.error import ParameterValueError
from astar_devopstool.version_announcement import get_version


def version_release_announcement_template(
        data_dict: dict,
        print_file=True,
        file_name=None,
        title=None,
        content='',
        *, encoding='utf-8'
) -> str:
    """
    发布通告模板
    :param data_dict:
    :param print_file: bool 是否输出为文件
    :param file_name:
    :param encoding: 文件编码格式
    :return:
    """
    if title:
        pass
    else:
        if 'project_name' not in data_dict:
            raise ParameterValueError("data_dict 必须有 `project_name`为名的键")
        else:
            project_name = data_dict.pop('project_name')
        if 'version' not in data_dict:
            raise ParameterValueError("data_dict 必须有 `version`为名的键")
        else:
            version = data_dict.pop('version')
            if isinstance(version, (tuple, list)):
                version = get_version(version)
        title = "{}-{}已发布！".format(project_name, version)

    if content:
        pass
    else:
        if 'content' not in data_dict:
            raise ParameterValueError("data_dict 必须有 `content`为名的键")
        else:
            content = data_dict.pop('content')

    s = ["|" + str(k) + "|" + str(v) + "|" for k, v in data_dict.items()]
    docs = '|信息|值|\n' + \
           '|:--:|:--:|\n' + \
           "\n".join(s)

    docs += '\n\n## 更新内容\n\n{}\n'.format(content)

    if print_file:
        auto_title(file_name, title=title, encoding=encoding)
        with open(file_name, "a+", encoding=encoding) as f:
            f.write(docs)
    return docs


def generate_readme_template_md(
        project_name,
        pypi_name=None,
        print_file=True,
        file_name=None,
        gitee=None,
        github=None,
        gitee_name=None,
        github_name=None,
        gitee_url=None,
        github_url=None,
        *, encoding='utf-8',
):
    """
    生成readme模板
    :param project_name: 项目名称
    :param pypi_name: pypi名称
    :param print_file: 是否打印出文件
    :param file_name: 文件名
    :param gitee: 有无gitee仓库
    :param github: 有无gitee仓库
    :param gitee_name: gitee仓库名
    :param github_name: github仓库名
    :param gitee_url:
    :param github_url:
    :return:
    """
    if pypi_name is None:
        pypi_name = project_name
    if gitee_name is None:
        gitee_name = project_name
    if github_name is None:
        github_name = project_name

    if gitee_url:
        li = gitee_url.rstrip('/').rsplit('/', 3)
        user_name, gitee_name = li[-2:]
        gitee_stars = "[![gitee](https://gitee.com/{user_name}/{gitee_name}/badge/star.svg)](https://gitee.com/snowlandltd/{gitee_name}/stargazers)\n".format(
            user_name=user_name, gitee_name=gitee_name)
        gitee = True
    elif gitee:
        gitee_stars = "[![gitee](https://gitee.com/{user_name}/{gitee_name}/badge/star.svg)](https://gitee.com/snowlandltd/{gitee_name}/stargazers)\n".format(
            user_name="snowlandltd", gitee_name=gitee_name)
    else:
        gitee_stars = ''
    if github_url:
        li = github_url.rstrip('/').rsplit('/', 3)
        user_name, github_name = li[-2:]
        github_stars = "[![github](https://img.shields.io/github/stars/{user_name}/{github_name})](https://img.shields.io/github/stars/{user_name}/{github_name})\n".format(
            user_name="astar-club", github_name=github_name)
    elif github:
        github_stars = "[![github](https://img.shields.io/github/stars/{user_name}/{github_name})](https://img.shields.io/github/stars/{user_name}/{github_name})\n".format(
            user_name="astar-club", github_name=github_name)
        github = True
    else:
        github_stars = ''

    docs = """
# {project_name}

[![version](https://img.shields.io/pypi/v/{pypi_name}.svg)](https://pypi.python.org/pypi/{pypi_name})
{gitee_stars}{github_stars}[![download](https://img.shields.io/pypi/dm/{pypi_name}.svg)](https://pypi.org/project/{pypi_name})
[![wheel](https://img.shields.io/pypi/wheel/{pypi_name}.svg)](https://pypi.python.org/pypi/{pypi_name})
![licence](https://img.shields.io/pypi/l/{pypi_name}.svg)
![status](https://img.shields.io/pypi/status/{pypi_name}.svg)





### 参考资料

[1] https://github.com/ASTARCHEN/astartool

[2] https://github.com/astar-club/astar-devopstool-python

    """.format(project_name=project_name,
               pypi_name=pypi_name,
               github_stars=github_stars,
               gitee_stars=gitee_stars)

    if print_file:
        auto_title(file_name, encoding=encoding, doc_type="md")
        with open(file_name, "a+", encoding=encoding) as f:
            f.write(docs)
    return docs


def generate_readme_template_rst(
        project_name,
        pypi_name=None,
        print_file=True,
        file_name=None,
        gitee=None,
        github=None,
        gitee_name: str = None,
        github_name: str = None,
        gitee_url: str = None,
        github_url: str = None,
        *, encoding='utf-8',
):
    """
    生成readme模板
    :param project_name: 项目名称
    :param pypi_name: pypi名称
    :param print_file: 是否打印出文件
    :param file_name: 文件名
    :param gitee: 有无gitee仓库
    :param github: 有无gitee仓库
    :param gitee_name: gitee仓库名
    :param github_name: github仓库名
    :param gitee_url:
    :param github_url:
    :return:
    """
    if pypi_name is None:
        pypi_name = project_name
    if gitee_name is None:
        gitee_name = project_name
    if github_name is None:
        github_name = project_name
    if gitee_url:
        li = gitee_url.strip('/').rsplit('/')
        user_name, gitee_name = li[-2:]
        gitee_stars = "\n.. |gitee| image:: https://gitee.com/{user_name}/{gitee_name}/badge/star.svg\n" \
                      "   :target: https://gitee.com/{user_name}/{gitee_name}/stargazers".format(
            user_name=user_name, gitee_name=gitee_name)
        gitee = True
    elif gitee:
        gitee_stars = "\n.. |gitee| image:: https://gitee.com/{user_name}/{gitee_name}/badge/star.svg\n" \
                      "   :target: https://gitee.com/snowlandltd/{gitee_name}/stargazers".format(
            user_name="snowlandltd", gitee_name=gitee_name)
    else:
        gitee_stars = ''

    if github_url:
        li = github_url.rstrip('/').rsplit('/')
        user_name, github_name = li[-2:]
        github_stars = "\n.. |github| image:: https://img.shields.io/github/stars/{user_name}/{github_name}\n" \
                       "   :target: https://img.shields.io/github/stars/{user_name}/{github_name})".format(
            user_name=user_name, github_name=github_name)
        github = True
    elif github:
        github_stars = "\n.. |github| image:: https://img.shields.io/github/stars/{user_name}/{github_name}\n" \
                       "   :target: https://img.shields.io/github/stars/{user_name}/{github_name})".format(
            user_name='astar-club', github_name=github_name)
    else:
        github_stars = ''

    docs = """{project_name}
{line}

|version| """.format(project_name=project_name, line='=' * 2 * len(project_name)) \
           + ("|gitee| " if gitee else '') + ("|github| " if github else "") + \
           """|download| |wheel| |license| |status|
           
           
           
           
           参考资料
           ~~~~~~~~
           
           [1] https://github.com/ASTARCHEN/astartool
           
           [2] https://github.com/astar-club/astar-devopstool-python
           
           .. |version| image:: https://img.shields.io/pypi/v/{pypi_name}.svg
              :target: https://pypi.python.org/pypi/{pypi_name}{gitee_stars}{github_stars}
           .. |download| image:: https://img.shields.io/pypi/dm/{pypi_name}.svg
              :target: https://pypi.org/project/{pypi_name}
           .. |wheel| image:: https://img.shields.io/pypi/wheel/{pypi_name}.svg
              :target: https://pypi.python.org/pypi/{pypi_name}
           .. |license| image:: https://img.shields.io/pypi/l/{pypi_name}.svg
           .. |status| image:: https://img.shields.io/pypi/status/{pypi_name}.svg
           
               """.format(project_name=project_name,
               line='=' * 2 * len(project_name),
               pypi_name=pypi_name,
               github_stars=github_stars,
               gitee_stars=gitee_stars)

    if print_file:
        auto_title(file_name, encoding=encoding, doc_type='rst')
        with open(file_name, "a+", encoding=encoding) as f:
            f.write(docs)
    return docs


def generate_readme_template(
        project_name,
        pypi_name=None,
        print_file=True,
        file_name=None,
        gitee=None,
        github=None,
        gitee_name=None,
        github_name=None,
        gitee_url=None,
        github_url=None,
        *, encoding='utf-8',
        doc_type='markdown'
):
    if doc_type.lower() in ('md', 'markdown'):
        generate_readme_template_md(
            project_name=project_name,
            pypi_name=pypi_name,
            print_file=print_file,
            file_name=file_name,
            gitee=gitee,
            github=github,
            gitee_name=gitee_name,
            github_name=github_name,
            gitee_url=gitee_url,
            github_url=github_url,
            encoding=encoding
        )
    else:
        generate_readme_template_rst(
            project_name=project_name,
            pypi_name=pypi_name,
            print_file=print_file,
            file_name=file_name,
            gitee=gitee,
            github=github,
            gitee_name=gitee_name,
            github_name=github_name,
            gitee_url=gitee_url,
            github_url=github_url,
            encoding=encoding
        )
