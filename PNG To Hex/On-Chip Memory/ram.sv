
module  frameRAM
(
		input [4:0] data_In,
		input [18:0] write_address, read_address,
		input we, Clk,

		output logic [4:0] data_Out
);

logic [<NUMBE_OF_BITS_PER_PIXEL - 1>:0] mem [0:<NUMBER_OF_PIXELS -1>]; 				// Frame buffer through the use of onchip memory

initial
begin
	 $readmemh("SpriteText/<INSERT_NAME_OF_TXT_FILE>", mem);
end


always_ff @ (posedge Clk) begin
	if (we)
		mem[write_address] <= data_In;
	data_Out<= mem[read_address];
end

endmodule