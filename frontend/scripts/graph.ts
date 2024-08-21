import { Dimensions } from "react-native"

export const Calculate_Dimensions = (Margin: number, Width_Subtraction: number, Height_Divisble: number) =>
{
    const SVG_Width = Dimensions.get('window').width - Width_Subtraction
    const SVG_Height = Dimensions.get('window').height / Height_Divisble

    const Double_Margin = Margin * 2

    const Graph_Width = SVG_Width - Double_Margin
    const Graph_Height = SVG_Height - Double_Margin

    return {SVG_Width, SVG_Height, Margin, Graph_Width, Graph_Height}
}