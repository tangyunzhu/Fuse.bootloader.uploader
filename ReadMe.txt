
2015.12.15	Fuse and Bootloader uploader v2
	Arduino uno	-->	Arduino Uno的Atmega328p
	328p_3V3_8M	-->	Arduino Pro or Mini
	Micro		-->	Arduino Micro's Atmega32u4
	leonardo	-->	Atmega32u4
	Xadow		-->	Atmega32u4
	Lite		-->	Atemga32u4
	Mega2560	-->	Genuino Mega's Atemga2560
	Seeed16u2	-->	Seeeduino v4's Atemga16u2
	Genuino16u2	-->	Genuino uno's Atemga16u2
	Mega16u2	-->	Genuino Mega's 16u2
	Atmega644p	-->	Atmega644p



2015.12.15	Fuse and Bootloader uploader v3
	追加ReadFlash按钮，可以读出芯片flash的所有内容，并保存为downflash.hex文件
	①点击"chip detect"按钮确认芯片信号
	②点击"Read Flash"按钮开始读出芯片flash内容



2015.12.16	Fuse and Bootloader uploader v4
	追加"Erase Chip"按钮，可以擦除flash内容
	"Read Flash"之前只能读取flash的内容，追加读出Fuse的功能, Fuse读出后将通过红色字体显示在界面下方

	Arduino uno	-->	Arduino Uno的Atmega328p
	328p_3V3_8M	-->	Arduino Pro or Mini
	Micro		-->	Arduino Micro's Atmega32u4
	leonardo	-->	Atmega32u4
	Xadow		-->	Atmega32u4
	Lite		-->	Atemga32u4
	Mega2560	-->	Genuino Mega's Atemga2560
	Seeed16u2	-->	Seeeduino v4's Atemga16u2
	Genuino16u2	-->	Genuino uno's Atemga16u2
	Mega16u2	-->	Genuino Mega's 16u2
	Atmega644p	-->	Atmega644p

	LogClear	-->	清除文本框中的所有数据
	Chip detect	-->	通过SPI接口检测单片机型号[在Write Flash/Read Flash/Erase Flash之前必须先检测单片机型号]
	Read Flash	-->	读取单片机Flash和Fuse
	Write Flash	-->	写入读出的flash文件.只写入flash文件，不管Fuse.执行此命名之前必须先读出flash才可以.
	Erase Flash	-->	擦除flash文件