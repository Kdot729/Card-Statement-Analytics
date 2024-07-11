import Svg, { Path } from "react-native-svg"
import {View, Text, Button, StyleSheet} from 'react-native';
import { useState } from 'react';
import * as DocumentPicker from 'expo-document-picker';
import { AxiosInstance } from "../../scripts/axios_interceptor";
import { Table } from "./table/table";
import { Create_Context } from "../../scripts/hook/context";
import React from "react";
import * as FileSystem from 'expo-file-system';

const Upload = (properties) =>
{
    return  <Svg xmlns="http://www.w3.org/2000/svg" width={384} height={384} viewBox="0 0 24 24" {...properties}>
                <Path
                fill="#369af2"
                d="M15 4H5v16h14V8h-4zM3 2.992C3 2.444 3.447 2 3.999 2H16l5 5v13.993A1 1 0 0 1 20.007 22H3.993A1 1 0 0 1 3 21.008zM13 12v4h-2v-4H8l4-4 4 4z"/>
            </Svg>
}

export const File = () =>
{
    const [PDF_ID, Set_PDF_ID] = useState("")

    const Upload_File = async () => 
    {
        try
        {
            const PDF_Document = await DocumentPicker.getDocumentAsync({type: 'application/pdf'})
            const PDF = PDF_Document.assets[0].uri
            const Base64_PDF = await FileSystem.readAsStringAsync(PDF, {encoding: FileSystem.EncodingType.Base64})
            const ID = Base64_PDF.substring(Base64_PDF.length - 16).slice(0,-1)

            Set_PDF_ID(ID)
            await AxiosInstance.post("post/PDF", {PDF_ID: ID, PDF: Base64_PDF})
        }
        catch (error) 
        {
            console.log("Error while selecting file: ", error.response.data);
        }
    }

    return  PDF_ID ? 
            <Create_Context.Provider value={PDF_ID}>
                <Table />
            </Create_Context.Provider > : 
            <View>
                <Text style={Styles.Header}>Upload PDF</Text>
                <Upload />
                <Button title="Select Document" onPress={Upload_File}/>
            </View>
}

const Styles = StyleSheet.create(
{
    Header:    {
                    color: 'black',
                    fontSize: 28,
                    textAlign: 'center',
                    marginVertical: 40,
                }

})

export default File