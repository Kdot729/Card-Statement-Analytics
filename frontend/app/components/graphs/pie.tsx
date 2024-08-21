import React from 'react'
import Svg, { Path, G, Text } from "react-native-svg"
import { useFetch } from '@/scripts/fetch';
import { Use_Context, Create_Context } from '@/scripts/hook/context';
import { arc, ascending, pie } from 'd3';
import { Calculate_Dimensions } from '@/scripts/graph';

const Pie = () => 
{
    const {SVG_Width, SVG_Height} = Calculate_Dimensions(0, 0, 2)
    
    const Radius = 7.7
    const PDF_ID = Use_Context(Create_Context)
    const {Pie} = useFetch("get/pie/PDF", PDF_ID)
    
    const Pie_Generator = pie().value((Transaction) => {return Transaction.Amount}).sort(ascending)

    const Pie_Data = Pie_Generator(Pie ?? [])
    const Arc_Generator = arc()

    const Pie_Graph = Pie_Data.map(({data: {Amount, Color, ID, Percentage}, endAngle, startAngle}) =>
    {
        
        const Pie_Arc = Create_Arc(0, Radius, startAngle, endAngle)
        const Pie_Path = Arc_Generator(Pie_Arc)

        const Inflextion_Radius = Radius + 0.5
        const Inflextion_Arc = Create_Arc(Inflextion_Radius, Inflextion_Radius, startAngle, endAngle)

        const [X_Inflextion, Y_Inflextion] = Arc_Generator.centroid(Inflextion_Arc)

        const X_Position_Sign = X_Inflextion > 0
        const Adjusted_X_Inflextion = X_Inflextion + 3 * ((X_Position_Sign ? 0.3 : -0.3))

        const Percent_Label = `${Percentage}%`
        const Rotate_Text = `rotate(-45, ${Adjusted_X_Inflextion}, ${Y_Inflextion})`

        return <G key={ID}>
                    <Path d={Pie_Path} fill={Color}/>
                    <Text x={Adjusted_X_Inflextion} y={Y_Inflextion}
                        transform={Rotate_Text}
                        textAnchor="middle" fill="rgb(246, 26, 246)" fontWeight="bold" fontSize={0.9}>
                    {Percent_Label}
                    </Text>
                </G>
    })

    const ViewBox = `0 0 ${SVG_Width / 20} ${SVG_Height / 20}`
    return  <Svg height={SVG_Height} width={SVG_Width} viewBox={ViewBox}>
                <G transform={`translate(${SVG_Width / 40}, ${10})`}>
                    {Pie ? Pie_Graph : null}
                </G>
            </Svg>
}

const Create_Arc = (innerRadius, outerRadius, startAngle, endAngle) =>
{
    return {innerRadius, outerRadius, startAngle, endAngle}
}

export default Pie
