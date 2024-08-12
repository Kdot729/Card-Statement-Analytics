import { Calculate_Linear_Domain } from '@/scripts/axis'
import { useFetch } from '@/scripts/fetch'
import { Use_Context, Create_Context } from '@/scripts/hook/context'
import { scaleBand, scaleLinear } from 'd3'
import React from 'react'
import { Dimensions } from 'react-native'
import Svg, { G, Text, Rect, Line } from "react-native-svg"

export const Bar = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const {Bar} = useFetch("get/bar/PDF", PDF_ID)

    const SVG_Width = Dimensions.get('window').width
    const SVG_Height = Dimensions.get('window').height / 2

    const Margin = 7
    const Double_Margin = Margin * 2

    const Graph_Width = SVG_Width - Double_Margin
    const Graph_Height = SVG_Height - Double_Margin

    const Text_FontSize = 12

    const Bar_Categories = Bar ? Bar.sort((First_Element, Second_Element) => 
    {
        return Second_Element.Amount - First_Element.Amount
    }).map((d) => d.ID) : []

    const Y_ScaleBand = scaleBand()
                        .domain(Bar_Categories)
                        .range([0, Graph_Height])
                        .padding(0.2)

    const Buffer_Domain_Number = Calculate_Linear_Domain(Bar, "Amount", SVG_Width)

    const X_ScaleLinear = scaleLinear()
                    .domain([-Buffer_Domain_Number, Buffer_Domain_Number])
                    .range([0, Graph_Width])

    const Align_Baseline = "central"

    const Vertical_Bars = Bar ? Bar.map(({ID, Amount, Color}) => 
    {
        const Rect_X_Coordinate = X_ScaleLinear(Math.min(Amount, 0))
        const Rect_Y_Coordinate = Y_ScaleBand(ID) || 0

        const Bar_Width = Math.abs(X_ScaleLinear(Amount) - X_ScaleLinear(0))
        const Bar_Height = Y_ScaleBand.bandwidth()

        const RGB_Black = "rgb(0, 0, 0)"

        const Label = `$${Amount}`
        const Text_Length = Amount.toString().length

        const Positive_X_Axis_Coordinate = Rect_X_Coordinate + Bar_Width + (Text_Length * 8)
        const Negative_X_Axis_Coordinate = Rect_X_Coordinate - (Text_Length * 0.5)
        const Text_X_Coordinate = Amount > 0 ? Positive_X_Axis_Coordinate : Negative_X_Axis_Coordinate
        const Text_Y_Coordinate = Rect_Y_Coordinate + Bar_Height / 2

        return <G key={ID}>
                    <Rect x={Rect_X_Coordinate} y={Rect_Y_Coordinate}
                        width={Bar_Width} height={Bar_Height}
                        stroke={RGB_Black} fill={Color} strokeWidth={1} rx={1}/>
                    <Text x={Text_X_Coordinate} y={Text_Y_Coordinate}
                        textAnchor="end" alignmentBaseline={Align_Baseline}
                        fill={RGB_Black} fontSize={Text_FontSize}>
                    {Label}
                    </Text>
                </G>
    }) : null

    const Grid_Lines = X_ScaleLinear.ticks(10).map((X_Tick) => 
    {

        const Tick_X_Coordinate = X_ScaleLinear(X_Tick)

        return  <G key={X_Tick}>
                    <Line x1={Tick_X_Coordinate} x2={Tick_X_Coordinate}
                        y1={0} y2={Graph_Height}
                        stroke="rgb(128, 128, 128)" opacity={0.2}/>
                    <Text x={Tick_X_Coordinate} y={Graph_Height + 10}
                        textAnchor="middle" alignmentBaseline={Align_Baseline}
                        fontSize={Text_FontSize} fontWeight="bold">
                    {X_Tick}
                    </Text>
                </G>
    })

    return  <Svg width={SVG_Width} height={SVG_Height + Text_FontSize}>
                <G width={Graph_Width} height={Graph_Height}
                    transform={`translate(${Margin}, ${Margin})`}>
                    {Grid_Lines}
                    {Vertical_Bars}
                </G>
            </Svg>
}

export default Bar