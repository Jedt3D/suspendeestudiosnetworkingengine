network_connect_tcp("127.0.0.1",14579);

network_listen("event",scr_print);
network_emit("authentication",quick_json("data","1234561"));


