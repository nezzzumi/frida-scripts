const modules = Process.enumerateModules();

modules.forEach((mod) => console.log(`name: ${mod.name}\nbase: ${mod.base}\n`));