import { FlatList } from 'react-native'
import React from 'react'
import Table_Header from './header'
import Table_Body from './body'
import { useFetch } from '@/scripts/fetch'
import { Use_Context, Create_Context } from '@/scripts/hook/context'
import { useSelector } from 'react-redux'

const Table_Flatlist = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const { URL } = useSelector((state) => state["Sorting"])
    const {Statistic, Color} = useFetch(URL, PDF_ID)

    const Render_Component = ({item}) => <Table_Body Row_Data={item} Row_Colors={Color} />

    return <FlatList data={Statistic} ListHeaderComponent={<Table_Header />} 
                keyExtractor={(Transaction) => Transaction["ID"]} 
                renderItem={Render_Component} scrollEnabled={false} />
}

export default Table_Flatlist