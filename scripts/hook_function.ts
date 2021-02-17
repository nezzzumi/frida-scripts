"use strict";

const libname = "libil2cpp.so";

function hook(function_address) {
    console.log("[i] Hooking...");
    Interceptor.attach(function_address, {
        onEnter: (args) => {
            //console.log(args[1].readPointer().readCString());
            send(args);
        },
        onLeave: (retval) => {
            send(retval);
        }
        
    });
}

var int = setInterval(() => {
    try {
        if (Process.getModuleByName(libname) != null) {
            console.log(`[+] ${libname} encontrada.`);
            const lib_base = Process.getModuleByName(libname).base;
            //const function_address = lib_base.add("0x118EA60"); ok
            const function_address = lib_base.add("0x118FF18");
    
            hook(function_address);
            clearInterval(int);
        }    
    } catch (error) {}
}, 1000);

console.log(`[i] Waiting for ${libname}...`);