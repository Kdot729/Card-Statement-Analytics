import Svg, { Path } from "react-native-svg"

export const File_Upload = (properties) =>
{
    return <Svg xmlns="http://www.w3.org/2000/svg" width={384} height={384} viewBox="0 0 24 24" {...properties}>
                <Path
                fill="#369af2"
                d="M15 4H5v16h14V8h-4zM3 2.992C3 2.444 3.447 2 3.999 2H16l5 5v13.993A1 1 0 0 1 20.007 22H3.993A1 1 0 0 1 3 21.008zM13 12v4h-2v-4H8l4-4 4 4z"/>
            </Svg>
}

export default File_Upload