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
local lines = lines_from(file)

local row_len = string.len(lines[1])
local col_len = #lines

local positions = {}

for i = 1, row_len do
	positions[i] = {}
	for j = 1, col_len do
		positions[i][j] = string.sub(lines[i], j, j)
	end
end

local dictionary = {}

local isalnum = function(str)
	return str:match("%w") ~= nil
end

for i = 1, row_len do
	for j = 1, col_len do
		if not isalnum(positions[i][j]) then
			goto continue1
		end
		if dictionary[positions[i][j]] == nil then
			dictionary[positions[i][j]] = { { i, j } }
		else
			table.insert(dictionary[positions[i][j]], { i, j })
		end
		::continue1::
	end
end

local count = 0

local indicator = {}

for i = 1, row_len do
	indicator[i] = {}
	for j = 1, col_len do
		indicator[i][j] = 0
	end
end

for _, x in pairs(dictionary) do
	for a = 1, #x do
		for b = 1, #x do
			if a == b then
				goto continue2
			end
			local start_point = x[a]
			local end_point = x[b]

			local diff_x = end_point[1] - start_point[1]
			local diff_y = end_point[2] - start_point[2]

			local proposed_x_first = start_point[1] - diff_x
			local proposed_y_first = start_point[2] - diff_y

			local proposed_x_second = end_point[1] + diff_x
			local proposed_y_second = end_point[2] + diff_y

			if
				proposed_x_first > 0
				and proposed_x_first <= row_len
				and proposed_y_first > 0
				and proposed_y_first <= col_len
				and indicator[proposed_x_first][proposed_y_first] == 0
			then
				indicator[proposed_x_first][proposed_y_first] = 1
				count = count + 1
			end
			if
				proposed_x_second > 0
				and proposed_x_second <= row_len
				and proposed_y_second > 0
				and proposed_y_second <= col_len
				and indicator[proposed_x_second][proposed_y_second] == 0
			then
				indicator[proposed_x_second][proposed_y_second] = 1
				count = count + 1
			end
		end
		::continue2::
	end
end

print(count)
