str = ""

File.open("words.txt", "r") do |fh|
    while(line = fh.gets) != nil
        str.concat(line.strip)
    end
end

puts str.length
