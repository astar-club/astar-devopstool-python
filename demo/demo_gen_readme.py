

from astar_devopstool.version_announcement._report import generate_readme_template


generate_readme_template("astar-devopstool",
                         file_name="README.md",
                         gitee=True,
                         github=True,
                         gitee_url="https://gitee.com/hoops/snowland-img2cartoon",
                         github_url="https://github.com/astar-club/astar-devopstool-python",
                         doc_type='md'
                         )
generate_readme_template("astar-devopstool",
                         file_name="README.rst",
                         gitee_url="https://gitee.com/snowlandltd/astar-devopstool-python",
                         github_url="https://github.com/astar-club/astar-devopstool-python",
                         doc_type='rst'
                         )