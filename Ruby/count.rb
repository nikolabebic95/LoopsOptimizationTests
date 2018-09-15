num = 0

File.open("words.txt", "r") do |fh|
    while(line = fh.gets) != nil
        num += line.strip.length
    end
end

puts num
