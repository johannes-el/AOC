local function file_exists(file)
	local f = io.open(file, "rb")
	if f then
		f:close()
	end
	return f ~= nil
end

local function lines_from(file)
	if not file_exists(file) then
		return {}
	end
	local lines = {}
	for line in io.lines(file) do
		lines[#lines + 1] = line
	end
	return lines
end

local file = "./input.txt"
local lines = lines_from(file)

local first_digit = 0
local last_digit = 0

local sum = 0

for _, v in pairs(lines) do
	for i = 0, #v do
		local char = v:sub(i, i)
		if char:match("%d") then
			first_digit = char
			break
		end
	end

	for i = #v, 1, -1 do
		local char = v:sub(i, i)
		if char:match("%d") then
			last_digit = char
			break
		end
	end
	sum = sum + tonumber(first_digit .. last_digit)
end

print(sum)
