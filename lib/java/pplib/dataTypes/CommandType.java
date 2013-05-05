package pplib.dataTypes;

public enum CommandType{
	New(100,"new"),
	List(101,"list"),

	Setup(200,"setup"),
	Draw(201,"draw"),
	Phase(202,"phase"),
	Turn(203,"turn"),
	Play(204,"play"),
	Out(205,"out"),
	Forfeit(206,"forfeit"),

	Test(300,"test"),
	Exit(301,"exit"),
	Close(301,"close");

	int intValue;
	String name;

	CommandType(int intValue, String name){
		this.intValue = intValue;
		this.name = name;
	}

	public int getInt(){
		return this.intValue;
	}
	public String toString(){
		return this.name;
	}

    public static CommandType getCommandType(String name){
        switch(name){
            case "new": return CommandType.New;
            case "list": return CommandType.List;
			case "setup": return CommandType.Setup;
			case "draw": return CommandType.Draw;
			case "phase": return Phase;
			case "turn": return Turn;
			case "play": return Play;
			case "out": return Out;
			case "test": return Test;
			case "exit": return Exit;
			case "close": return Close;
			case "forfeit": return Forfeit;
            default : return null;
        }
    }
}
