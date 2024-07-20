import React from 'react'
import { Table } from './table/table'
import { ScrollView } from 'react-native'
import Pie from './graphs/pie'

const Analytics = () => 
{ 
    return  <ScrollView >
                <Table />
                <Pie></Pie>
            </ScrollView>
}

export default Analytics