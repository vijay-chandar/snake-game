import cx_Freeze

executables = [cx_Freeze.Executable("Slither.py")]

cx_Freeze.setup(

	name = "Slither",
	options = { "build_exe": { "packages": ["pygame"], "include_files": ["Apple.png", "apple2.png", "arrowRight.png", "dead.jpg", "flash.jpg", "flash_and_arrow.jpg", "flashNarrow.jpg", "GoT.jpg", "pb.jpg", "scorecard.png", "scoreSymbol.png", "snakeBody.png", "SnakeHead.png", "SnakeTail.png", "thunder.jpg", "highscore.txt"] } },
	description = "Slither Game",
	executables = executables
	)