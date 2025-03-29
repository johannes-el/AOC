local file = io.open("./input.txt", "r")

if file then
	local sum = 0
	for line in file:lines() do
		local num = tonumber(line)
		local val = math.floor(tonumber(line) / 3) - 2

		while true do
			val = math.floor(tonumber(num) / 3) - 2
			num = val
			if val <= 0 then
				break
			end
			sum = sum + val
		end
	end

	print(sum)

	file:close()
else
	print("Failed to open file.")
end
