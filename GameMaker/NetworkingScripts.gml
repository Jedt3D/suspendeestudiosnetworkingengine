#define network_connect_tcp
global.listener = ds_map_create();
global.listenerlist = ds_list_create();
global.socket = network_create_socket(network_socket_tcp);
global.server = network_connect_raw(global.socket,argument0,argument1);
global.splitter = "~§~"


#define network_listen
//network_listen(path,script)
// In script do var name = argument0 and var data = argument1
//
var path = argument0;
var script = argument1;

ds_map_add(global.listener,path,script);
ds_list_add(global.listenerlist,path);


#define network_emit
// Network_Emit(Path,String)
//This will send either a raw JSON value or a raw text value of your choice automatically
var suspath = argument0;
var sustxt = argument1;

var susbuf = buffer_create(1024,buffer_grow,1);
buffer_seek(susbuf,buffer_seek_start,0);
var susmap = ds_map_create();

if (ds_exists(sustxt,ds_type_map) && !is_string(sustxt))
{
ds_map_add_map(susmap,suspath,sustxt);
}
else
{
    if (string_pos('{',sustxt) != 0 && string_pos('}',sustxt) != 0 && string_pos(':',sustxt) != 0)
    {
    ds_map_add(susmap,suspath,string_replace_all(sustxt,"'",'"'));
    }
    else
    {
    ds_map_add(susmap,suspath,sustxt);
    }

}


buffer_write(susbuf,buffer_text,json_encode(susmap)+global.splitter);
ds_map_destroy(susmap);
network_send_raw(global.socket,susbuf,buffer_tell(susbuf));
buffer_delete(susbuf);


#define network_process_packet
//Splitter is this ~§~
//Good example "Ok~§~banana~§~one~§~"
if (ds_map_find_value(async_load,'type') == network_type_data)
{
var buffer = ds_map_find_value(async_load,'buffer');
str = buffer_read(ds_map_find_value(async_load,'buffer'),buffer_text);

map = ds_map_create();
//show_message(str)
while (string_pos("~§~",str) != 0)
{

var susdat = json_decode( string_copy(str,0,string_pos("~§~",str)-1));

    for (i=0;i<ds_list_size(global.listenerlist);i++)
    {  var listenerlist = global.listenerlist[| i];
        if (susdat[? "path"] == listenerlist && ds_map_exists(susdat,listenerlist))
       { 
       
        script_execute( ds_map_find_value(global.listener, susdat[? "path"])
        ,susdat[? "path"],ds_map_find_value( susdat,listenerlist) 
        )
        }
       
    }
ds_map_destroy(susdat);
str = string_delete(str,1,string_pos("~§~",str)+2)
}
}


