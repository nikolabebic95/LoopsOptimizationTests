str = ""

File.foreach("words.txt") do |line|
    str.concat(line.strip)
end

puts str.length
