from graphviz import Digraph

dg = Digraph(format='png')

# dg.node('Eigen')
# dg.node('cereal')
# dg.node('stanmath')
# dg.node('cppad-codegen')
# dg.node('cmdline')
# dg.node('liburg')
# dg.node('matplotlibcpp')
# dg.node('pybind11')
# dg.node('gtkmm-3')
# dg.node('epoxy')
# dg.node('CPPurse')
#
dependencies = [["flier-metaprogramming", "Boost::boost",],
["flier-math", "Eigen", "flier-metaprogramming", "stanmath", "flier-quantity",],
["flier-quantity", "Eigen", "flier-metaprogramming", "flier-math",],
["flier-basic", "flier-math", "flier-metaprogramming", "Eigen", "flier-quantity", "cmdline", "stdc++fs",],
["flier-serialization", "flier-basic", "cereal",],
["flier-task", "flier-basic", "Boost::context",],
["flier-interprocess", "flier-basic", "rt",],
["flier-stream", "flier-basic", "Boost::iostreams", "atomic", "pthread", "stdc++fs",],
["flier-message", "flier-basic", "flier-serialization", "flier-stream", "rt",],
["flier-joypad", "flier-basic", "stdc++fs",],
["flier-urg3d", "urg", "pthread", "flier-estimation", "flier-quantity",],
["flier-urg2d", "flier-basic", "flier-quantity", "flier-device", "pthread", "stdc++fs",],
["flier-visualizer", "flier-basic", "Boost::iostreams", "PkgConfig::gtkmm", "PkgConfig::epoxy", "oglplus", "Eigen", "flier-transform", "matplotlibcpp", "flier-transform",],
["flier-py_shell", "flier-framework", "flier-emergency", "pybind11::module", "pybind11::lto",],
["flier-task", "flier-basic",],
["flier-stream", "flier-basic",],
["flier-message", "flier-basic", "flier-serialization", "flier-stream",],
["flier-urg2d", "flier-basic", "flier-quantity",],
["flier-emergency", "flier-message",],
["flier-multidiff", "flier-basic", "flier-quantity",],
["flier-transform", "flier-basic", "flier-quantity", "flier-multidiff",],
["flier-device", "flier-quantity", "flier-math", "flier-message", "flier-emergency",],
["flier-text_log",],
["flier-control", "flier-transform", "flier-task", "flier-centroid", "flier-estimation", "flier-emergency", "Eigen",],
["flier-regulator", "flier-multidiff", "Eigen", "flier-control_matrices",],
["flier-servo", "flier-control_matrices", "Eigen",],
["flier-control_matrices", "Eigen",],
["flier-oned_control", "flier-device", "flier-transform", "flier-regulator", "flier-task", "flier-centroid", "flier-estimation", "Eigen",],
["flier-estimation", "flier-basic", "Eigen",],
["flier-localization", "flier-quantity", "flier-device", "flier-transform", "flier-estimation",],
["flier-centroid", "flier-transform",],
["flier-robot_control", "flier-device", "flier-transform", "flier-regulator", "flier-task", "flier-centroid", "flier-estimation", "flier-message", "flier-codegen",],
["flier-bathyal",],
["flier-cway", "flier-device", "flier-serialization", "flier-bathyal",],
["flier-ecat", "flier-device", "flier-serialization",],
["flier-tosheet",],
["flier-multiple_test", "flier-ecat", "flier-cway", "flier-bathyal", "flier-framework", "cppurse",],
["flier-log_saver", "flier-message", "flier-bathyal",],
["flier-gazebo",],
["flier-framework",],
["flier-codegen",],
["flier-optimal_control", "flier-codegen", "flier-metaprogramming",]]

for i in dependencies:
    for j in range(1, len(i)):
        dg.edge(i[j], i[0])

dg.render("./dgraph", view=True)
dg.view()
