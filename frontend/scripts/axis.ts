import { extent } from "d3"

export const Calculate_Linear_Domain = (Graph_Data, Key, SVG_Dimension) =>
{

    const Axis_Value: number[] = Graph_Data ? Graph_Data.map((Data) => {return Data[Key]}) : [0, 0]
    let [Min, Max] = extent(Axis_Value)
    
    const Absolute_Min = Math.abs(Number(Min))
    Max = Number(Max)
    const Buffer_Axis = SVG_Dimension / 2

    const Domain_Number = Absolute_Min > Max ? Absolute_Min : Max

    return Domain_Number + Buffer_Axis
}