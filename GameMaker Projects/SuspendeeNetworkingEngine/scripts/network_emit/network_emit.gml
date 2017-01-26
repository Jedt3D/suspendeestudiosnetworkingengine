// Network_Emit(Path,String)
//This will send either a raw JSON value or a raw text value of your choice automatically
var suspath = argument0;
var sustxt = argument1;

var susbuf = buffer_create(1024,buffer_grow,1);
buffer_seek(susbuf,buffer_seek_start,0);
var susmap = ds_map_create();

if (ds_exists(sustxt,ds_type_map))
{
ds_map_add_map(susmap,suspath,sustxt);
}
else
{
ds_map_add(susmap,suspath,sustxt);
}


buffer_write(susbuf,buffer_text,json_encode(susmap)+global.splitter);
ds_map_destroy(susmap);
network_send_raw(global.socket,susbuf,buffer_tell(susbuf));
buffer_delete(susbuf);
