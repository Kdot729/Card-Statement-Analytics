import React from 'react'
import Svg, { G, Text, Rect } from "react-native-svg"
import { extent, interpolatePuBu, scaleSequential} from 'd3'
import { useFetch } from '@/scripts/fetch'
import { Use_Context, Create_Context } from '@/scripts/hook/context'
import { Calculate_Dimensions } from '@/scripts/graph'

export const Heatmap = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const {Heatmap} = useFetch("get/heatmap/PDF", PDF_ID)

    const {SVG_Width, SVG_Height, Margin, Graph_Width, Graph_Height} = Calculate_Dimensions(5, 25, 2.3)
    const Dimension = (Graph_Width * Graph_Height) / 2971.4217

    const Day_of_Weeks = []
    const Months = []
    const X_Axis_Ticks = []

    const Buffer_Dimension = Dimension + 2
    var X_Position = 0 + Buffer_Dimension
    var Y_Coordinate = Dimension / 2
    const Size = Buffer_Dimension / 1.5

    Heatmap ? Heatmap.map((Day_of_Month) => 
    {
        Day_of_Weeks.push(Day_of_Month["Day"])
        Months.push(Day_of_Month["Month"])

        Day_of_Month["X_Coordinate"] = X_Position + Size
        if (Day_of_Month["Day"] == "Sat")
            {X_Position += Buffer_Dimension}
    }) : null

    const Color_Scale = scaleSequential()
                        .interpolator(interpolatePuBu)
                        .domain(Heatmap ? extent(Heatmap, (data) => data["Sum"]) : [0, 0])
    
    const Day_of_Week_Y_Coorindate = {}
    Day_of_Weeks ? [...new Set(Day_of_Weeks)].map((Day) =>
    {
        Day_of_Week_Y_Coorindate[Day] = Y_Coordinate
        Y_Coordinate += Buffer_Dimension

        X_Axis_Ticks.push(<Text key={Day}
                            x={0} y={Day_of_Week_Y_Coorindate[Day] + Size} 
                            fontSize={Size}>{Day}</Text>)
    }) : null

    const Transform = `translate(${Graph_Width / 8}, ${Margin * 2})`

    const Heatmap_Bar = Heatmap ? Heatmap.map(({"Numbered Day": Numbered_Day, Sum, Day, X_Coordinate}) => 
    {
        const RGB_Black = "rgb(0, 0, 0)"
        const Round_Corners = 5

        const Y_Coordinate = Day_of_Week_Y_Coorindate[Day]
        return <G key={Numbered_Day}>
                    <Rect className={Day} x={X_Coordinate} y={Y_Coordinate}
                        width={Dimension} height={Dimension}
                        stroke={RGB_Black} fill={Color_Scale(Sum)} strokeWidth={1}
                        rx={Round_Corners} ry={Round_Corners}/>
                    <Text x={X_Coordinate + (Dimension / 2.85)} 
                        y={Y_Coordinate + (Dimension / 1.7857)} 
                        fontSize={Dimension / 4}>{Numbered_Day}</Text>
                </G>
    }) : null

    const Y_Axis_Tick = Months ? [...new Set(Months)].map((Month, index) =>
    {
        const Y_Tick_Divisible = (Dimension * 2) / 30
        const X_Coordinate = (Dimension * .444444) + (index * Dimension * 3.111) + Buffer_Dimension + Size

        return <Text key={Month}
                    x={X_Coordinate}
                    y={Dimension / Y_Tick_Divisible} fontSize={Size}>{Month}</Text>
    }) : null

    return  <Svg width={SVG_Width} height={SVG_Height}>
                <G width={Graph_Width} height={Graph_Height}
                    transform={Transform}>
                    <G>{Heatmap_Bar}</G>
                    <G>{X_Axis_Ticks}</G>
                    <G>{Y_Axis_Tick}</G>
                </G>
            </Svg>
}

export default Heatmap