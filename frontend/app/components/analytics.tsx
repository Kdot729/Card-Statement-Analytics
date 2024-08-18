import React from 'react'
import { Table } from './table/table'
import { ScrollView } from 'react-native'
import Pie from './graphs/pie'
import Bar from './graphs/bar'
import LineGraph from './graphs/line'
import Heatmap from './graphs/heatmap'

const Analytics = () => 
{ 
    return  <ScrollView >
                <Table />
                <LineGraph />
                <Heatmap />
                <Bar />
                <Pie />
            </ScrollView>
}

export default Analytics