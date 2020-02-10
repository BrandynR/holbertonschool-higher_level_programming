#!/usr/bin/node

exports.esrever = function (list) {
  const new_list = [];
  let iter = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    new_list[iter] = list[i];
    iter += 1;
  }
  return (new_list);
};
