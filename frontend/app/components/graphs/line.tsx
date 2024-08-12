import React from 'react'
import Svg, { G, Path, Line, Text, Rect } from "react-native-svg"
import { Dimensions } from 'react-native'
import { line, extent, scaleLinear, scaleTime, timeFormat, } from 'd3'
import { useFetch } from '@/scripts/fetch'
import { Use_Context, Create_Context } from '@/scripts/hook/context'

const Margin = 5
const SVG_Width = Dimensions.get('window').width - 25
const SVG_Height = Dimensions.get('window').height / 2

const Adjusted_X_Coordinate = 40 + Margin
const Double_Margin = Margin * 2
const Graph_Width = SVG_Width - Double_Margin
const Graph_Height = SVG_Height - Double_Margin

export const LineGraph = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const {Line} = useFetch("get/line/PDF", PDF_ID)

    const Dates = Line ? Line.map((Day_of_Month) => {return new Date(Day_of_Month["Transaction Date"])}) : [new Date(), new Date()]
    let [Minumum_Date, Maximum_Date] = extent(Dates)

    const Daily_Sums: number[] = Line ? Line.map((Day_of_Month) => {return Day_of_Month["Sum"]}) : [0, 0]
    let [Min, Max] = extent(Daily_Sums)
    
    const Absolute_Min = Math.abs(Number(Min))
    Max = Number(Max)
    const Buffer_Axis = SVG_Width / 2

    const Domain_Number = Absolute_Min > Max ? Absolute_Min : Max
    const Buffer_Domain_Number = Domain_Number + Buffer_Axis

    const Y_Scale = scaleLinear()
                        .domain([-Buffer_Domain_Number, Buffer_Domain_Number])
                        .range([Graph_Height, 0]);

    const X_Scale = scaleTime()
                    .domain([Minumum_Date, Maximum_Date])
                    .range([0, Graph_Width - 50])

    const Building_Line = line()
                            .x((Day_of_Month) => 
                            {
                                const X_Line_Coordinate = X_Scale(new Date(Day_of_Month["Transaction Date"])) + Adjusted_X_Coordinate
                                Day_of_Month["Rectangle X"] = X_Line_Coordinate - 4
                                return X_Line_Coordinate
                            })
                            .y((Day_of_Month) => 
                            {
                                const Y_Line_Coordinate = Y_Scale(Day_of_Month["Sum"])
                                return Y_Line_Coordinate
                            })

    const Line_Path = Building_Line(Line ?? [])

    const X_Axis = Scale_Linear_X_Axis(X_Scale)
    const Y_Axis = Scale_Linear_Y_Axis(Y_Scale)

    const Transform = `translate(0, ${Margin})`

    const Rectangles =  Line ? Line.map((Value, index) =>
    {
        var Cumulative_Sum = 0
        const Grouped_Rectangles = Value["Grouped Transactions"].map(({ID, Amount, Color}, index) =>
        {
            const Dimension = 7
            const Y_Scale_Number = Amount + Cumulative_Sum
            const Y_Coordinate = Y_Scale(Y_Scale_Number) - 1

            Cumulative_Sum = Y_Scale_Number
            return <Rect key={index} x={Value["Rectangle X"]} y={Y_Coordinate} fill={Color}
                width={Dimension} height={Dimension}/>
        })

        return <G key={index}>{Grouped_Rectangles}</G>
    }) : []

    return  <Svg width={SVG_Width} height={SVG_Height + 15}>
                <G width={Graph_Width} height={Graph_Height}
                transform={Transform}>
                    <Path d={Line_Path} opacity={1}
                        stroke="rgb(0, 0, 0)" fill="none" strokeWidth={2}/>
                    {Rectangles}
                    {X_Axis}
                    {Y_Axis}
                </G>
            </Svg>
}

export const Scale_Linear_Y_Axis = (Y_Scale) =>
{
    const Render_Y_Axis = 
        Y_Scale
        .ticks()
        .map((Y_Tick_Value) => 
        {
            const Y_Coordinate_to_Translate = Y_Scale(Y_Tick_Value) || 0
            const Translate_Group_Element = `translate(35, ${Y_Coordinate_to_Translate})`
            
            const Line_Properties = {x1: 8, x2: SVG_Width}
            const Text_Properties = {x: -5, y: 0}
            return <Tick ClassName="y-tick" key={Y_Tick_Value} Transform={Translate_Group_Element} 
                        Line_Properties={Line_Properties} Text_Properties={Text_Properties} 
                        Value={Y_Tick_Value} />
        })

    return  <G id="y-tick-container">
                {Render_Y_Axis}
            </G>
}

export const Scale_Linear_X_Axis = (X_Scale) =>
{
    const Ending_Tick_Position = SVG_Height - 120
    const Starting_Tick_Position = Ending_Tick_Position - 11

    const Render_X_Axis = 
    X_Scale
    .ticks()
    .map((X_Tick_Value) => 
    {
        const Day_of_Month = timeFormat("%d")(X_Tick_Value).toString().replaceAll("0", "")
        const Calculated_X_Coordinate = X_Scale(X_Tick_Value) + Adjusted_X_Coordinate

        const Translate_Group_Element= `translate(${Calculated_X_Coordinate}, ${SVG_Height / 4})`

        const Line_Properties = {y1: Starting_Tick_Position, y2: Ending_Tick_Position}
        const Text_Properties = {dy: ".71em", y: Ending_Tick_Position}
        return <Tick ClassName="x-tick" key={X_Tick_Value} Transform={Translate_Group_Element} 
                    Line_Properties={Line_Properties} Text_Properties={Text_Properties} 
                    Value={Day_of_Month} />
    })

    return  <G id="x-tick-container">
                {Render_X_Axis} 
            </G>
}

const Tick = ({ClassName, Transform, Line_Properties, Text_Properties, Value}) => 
{
    return  <G className={ClassName} transform={Transform}>
                <Line {...Line_Properties} stroke="rgb(90, 90, 90)" strokeWidth="1"/>
                <Text style={{ textAnchor: 'middle' }} {...Text_Properties}>{Value}</Text>
            </G>
}

export default LineGraph