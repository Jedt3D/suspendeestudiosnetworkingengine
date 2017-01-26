//network_listen(path,script)
// In script do var name = argument0 and var data = argument1
//
var path = argument0;
var script = argument1;

ds_map_add(global.listener,path,script);
ds_list_add(global.listenerlist,path);
