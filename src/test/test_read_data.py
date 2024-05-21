import os
from caret_analyze import Architecture, Lttng, Application
# from caret_analyze.plot import Plot


def test_read_data():
    trace_data = os.path.expanduser('~/.ros/tracing/session-20240417161654')
    # trace_data = os.path.expanduser('~/CARET_ws/architecture_reader/e2e_sample_interPolingTest')
    lttng = Lttng(trace_data, force_conversion=False)
    arch = Architecture('lttng', trace_data)
    arch.export('arch_autoware_data.yaml', force=True)
    # arch.export('arch_sample_sub_intersub_test.yaml', force=True)
    # arch.export('new_arch_autware_data.yaml', force=True)

    print('create app from Lttng')
    app = Application(arch, lttng)
    print('Load arch from yaml')
    # arch_from_yaml = Architecture('yaml', 'arch_sample_sub_intersub_test.yaml')
    arch_from_yaml = Architecture('yaml', 'arch_autoware_data.yaml')
    print('create app from yaml')

    # paths = arch_from_yaml.search_paths('/minimal_publisher','/minimalSubscriber')
    # path = paths[0]
    # arch_from_yaml.add_path('target', path)
    # arch_from_yaml.export('add_path_arch_sample_sub_intersub_test.yaml', force=True)
    # arch = Architecture('yaml', 'add_path_arch_sample_sub_intersub_test.yaml')
    # path = arch.get_path('target')
    # path.verify()
    # app = Application(arch,lttng)
    # target_path = app.get_path('target')
    # plot = Plot.create_message_flow_plot(target_path)
    # plot.show()
    # print('OK')
    # assert True