global.listener = ds_map_create();
global.listenerlist = ds_list_create();
global.socket = network_create_socket(network_socket_tcp);
global.server = network_connect_raw(global.socket,argument0,argument1);
global.splitter = "~§~"
