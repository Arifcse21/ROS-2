from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arifcse21',
    maintainer_email='arifcse21@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main",
            "speaker_node = my_py_pkg.speaker_node:main",
            "robot_news_station = my_py_pkg.Publishers.robot_news_station:main",
            "net_speed_test = my_py_pkg.Publishers.internet_speed_tester:main",
            "smartphone = my_py_pkg.Subscribers.smartphone:main",
        ],
    },
)
