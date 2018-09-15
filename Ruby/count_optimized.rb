num = 0

File.foreach("words.txt") do |line|
    num += line.strip.length
end

puts num
