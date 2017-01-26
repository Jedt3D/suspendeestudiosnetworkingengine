//Splitter is this ~§~
//Good example "Ok~§~banana~§~one~§~"

if (ds_map_find_value(async_load,"type") == network_type_data)
{
var buffer = ds_map_find_value(async_load,"buffer");
str = buffer_read(ds_map_find_value(async_load,"buffer"),buffer_text);

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
        ,susdat[? "path"],ds_map_find_value( susdat,susdat[? "path"]) 
        )
        }
       
    }
ds_map_destroy(susdat);
str = string_delete(str,1,string_pos("~§~",str)+2)
}
}
