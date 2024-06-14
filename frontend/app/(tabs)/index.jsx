
import {View, Text, Button, StyleSheet} from 'react-native';
import React, { useState } from 'react';
import {DocumentPicker} from 'expo-document-picker';
import File_Upload from '../components/file_upload';

export default function App() 
{

    const [Document, Set_Document] = useState("")

    const Upload_File = async () => 
    {
        const Document = await DocumentPicker.getDocumentAsync({type: 'application/pdf'})
        Set_Document(Document)
    }

    return  (
            <View>
                <View>
                    <Text style={Styles.Header}>Upload file</Text>
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