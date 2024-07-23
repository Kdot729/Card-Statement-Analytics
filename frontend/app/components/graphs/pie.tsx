import React from 'react'
import Svg, { Path, G } from "react-native-svg"
import { useFetch } from '@/scripts/fetch';
import { Use_Context, Create_Context } from '@/scripts/hook/context';
import {Dimensions} from 'react-native';
import { arc, pie } from 'd3';

const Pie = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const {Pie} = useFetch("get/pie/PDF", PDF_ID)
    const Phone_Width = Dimensions.get('window').width
    
    const Pie_Generator = pie().value((Transaction) => {return Transaction.Amount})
    const Pie_Data = Pie_Generator(Pie ?? [])

    const Pie_Arcs = Pie_Data.map(({data: {Amount, Color, ID, Percentage}, endAngle, startAngle}) =>
    {

        const Arc = arc()({
                        innerRadius: 0,
                        outerRadius: 8,
                        startAngle: startAngle,
                        endAngle: endAngle,
                    })

        return  {Amount, Color, ID, Percentage, Path: Arc}
    })

    const Pie_Graph = Pie_Arcs.map((Arc, index) => 
    {
        return  <G key={index}>
                    <Path d={Arc["Path"]} fill={Arc["Color"]}/>
                </G>
    })

    return  <Svg height="1000" width="1000" viewBox='0 0 50 50'>
                <G transform={`translate(${Phone_Width / 40}, ${10})`}>
                    {Pie ? Pie_Graph : null}
                </G>
            </Svg>
}

export default Pie