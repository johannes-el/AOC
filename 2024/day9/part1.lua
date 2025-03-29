local function file_exists(file)
	local f = io.open(file, "r")
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
local input = lines_from(file)[1]

local id = 0

local new_tab = {}

for i = 1, #input do
	if i % 2 ~= 0 then
		for _ = 1, tonumber(string.sub(input, i, i)) do
			table.insert(new_tab, id)
		end
		id = id + 1
	else
		for _ = 1, tonumber(string.sub(input, i, i)) do
			table.insert(new_tab, ".")
		end
	end
end

local i = 1
local j = #new_tab

while i < j do
	if new_tab[j] == "." then
		j = j - 1
	elseif new_tab[i] == "." then
		new_tab[i], new_tab[j] = new_tab[j], new_tab[i]
		i = i + 1
		j = j - 1
	else
		i = i + 1
	end
end

local sum = 0

for x = 1, #new_tab do
	if new_tab[x] ~= "." then
		sum = sum + (x - 1) * tonumber(new_tab[x])
	end
end

print(sum)
