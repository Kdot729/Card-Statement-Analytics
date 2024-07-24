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
    const Arc_Generator = arc()

    const Pie_Graph = Pie_Data.map(({data: {Amount, Color, ID, Percentage}, endAngle, startAngle}) =>
    {
        const Pie_Slice =   {
                                innerRadius: 0,
                                outerRadius: 8,
                                startAngle,
                                endAngle
                            }

        const Pie_Path = Arc_Generator(Pie_Slice)

        return <G key={ID}>
                    <Path d={Pie_Path} fill={Color}/>
                </G>
    })

    return  <Svg height="1000" width="1000" viewBox='0 0 50 50'>
                <G transform={`translate(${Phone_Width / 40}, ${10})`}>
                    {Pie ? Pie_Graph : null}
                </G>
            </Svg>
}

export default Pie