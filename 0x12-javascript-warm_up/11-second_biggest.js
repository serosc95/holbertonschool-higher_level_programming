#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const allargs = process.argv;
  const args = allargs.slice(2, allargs.length).sort();
  console.log(args[args.length - 2]);
}
