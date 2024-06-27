
import {View, Text, Button, StyleSheet} from 'react-native';
import React, { useState } from 'react';
import * as DocumentPicker from 'expo-document-picker';
import File_Upload from '../components/file_upload';
import { AxiosInstance } from "../../scripts/axios_interceptor";

export default function App() 
{

    const [Document, Set_Document] = useState("")

    const Upload_File = async () => 
    {
        const PDF_Document = await DocumentPicker.getDocumentAsync({type: 'application/pdf'})
        Set_Document(PDF_Document)

        const PDF = PDF_Document.assets[0].uri
        const No_Header_PDF = PDF.split(",")[1]
        const PDF_Last_Characters = No_Header_PDF.substr(No_Header_PDF.length - 16);
        const PDF_ID = PDF_Last_Characters.slice(0,-1)

        await AxiosInstance.post("post/PDF", {PDF_ID, PDF})

    }

    return  (
            <View>
                <View>
                    <Text style={Styles.Header}>Upload PDF</Text>
                    <File_Upload />
                    <Button title="Select Document" onPress={Upload_File}/>
                </View>
            </View>
            )
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