#!/usr/bin/env ruby
arr = File.readlines('d01.in').map &:to_i
[1, 3].each do |i|
    puts arr[0...-i].zip(arr[i..-1]).count{|x,y| x<y}
end