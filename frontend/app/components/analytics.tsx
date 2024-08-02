import React from 'react'
import { Table } from './table/table'
import { ScrollView } from 'react-native'
import Pie from './graphs/pie'
import Bar from './graphs/bar'

const Analytics = () => 
{ 
    return  <ScrollView >
                <Table />
                <Bar />
                <Pie></Pie>
            </ScrollView>
}

export default Analytics