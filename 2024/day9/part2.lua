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
-- local input = "03201"

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

local j = #new_tab

local sum = 0

while true do
	while j >= 1 and new_tab[j] == "." do
		j = j - 1
	end

	if j == 0 then
		break
	end

	local current_digit = new_tab[j]
	local count = 0

	while j >= 1 and new_tab[j] == current_digit do
		j = j - 1
		count = count + 1
	end

	local first_idx = 1
	local first_idx_set = false

	local dot_count = 0
	for x = 1, j do
		if new_tab[x] == "." then
			dot_count = dot_count + 1
			if not first_idx_set then
				first_idx_set = true
				first_idx = x
			end
		else
			first_idx_set = false
			dot_count = 0
		end

		if dot_count == count then
			-- Replace the dots with the current digit
			for k = first_idx, first_idx + dot_count - 1 do
				new_tab[k] = current_digit
			end
			-- Replace the current digit with the dots
			for u = j + 1, j + 1 + dot_count - 1 do
				new_tab[u] = "."
			end

			break
		end
	end
end

--print(table.concat(new_tab))

for x = 1, #new_tab do
	if new_tab[x] ~= "." then
		sum = sum + (x - 1) * tonumber(new_tab[x])
	end
end

print(sum)
